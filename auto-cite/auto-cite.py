from util import *
from importlib import import_module
import requests
import html


# config info for input/output files and plugins
config = {}
try:
    config = load_data("../_config.yaml", type_check=False).get("auto-cite")
    if not config:
        raise Exception("Couldn't find auto-cite config")
except Exception as message:
    log(message, 3, "red")
    exit(1)

log("Compiling list of sources to cite")

# compile master list of sources from various plugins
sources = []

# loop through plugins
for plugin in config.get("plugins", []):
    # get plugin props
    name = plugin.get("name", "-")
    files = plugin.get("input", "")

    # show progress
    log(f"Running {name} plugin")

    # loop through plugin input files
    for file in files:
        # show progress
        log(file, 2)

        # get data in file
        data = []
        try:
            data = load_data(file)
        except Exception as message:
            log(message, 3, "red")
            exit(1)

        plugin_sources = import_module(f"plugins.{name}").main(data)

        log(f"Got {len(plugin_sources)} sources", 2, "green")

        for source in plugin_sources:
            sources.append(source)

log("Generating citations for sources")

# load existing citations
citations = []
try:
    citations = load_data(config["output"])
except Exception as message:
    log(message, 2, "yellow")

# list of new citations to overwrite existing citations
new_citations = []

# --- Crossref → CSL mapper ---
def crossref_to_csl(crossref_json, source=None):
    """
    Convert Crossref JSON metadata into a minimal CSL-like dict,
    preserving custom fields from the original source (e.g., tags, image).
    
    Args:
        crossref_json (dict): The 'message' part of a Crossref API response.
        source (dict, optional): Original source dict from sources.yaml.
        
    Returns:
        dict: CSL-like citation dictionary.
    """
    csl = {}

    # --- DOI ---
    csl["id"] = crossref_json.get("DOI", "")

    # --- Title ---
    titles = crossref_json.get("title", [])
    csl["title"] = html.unescape(titles[0]) if titles else ""

    # --- Authors ---
    csl["authors"] = []
    for author in crossref_json.get("author", []):
        given = author.get("given", "")
        family = author.get("family", "")
        full_name = " ".join([given, family]).strip()
        if full_name:
            csl["authors"].append(full_name)

    # --- Publisher / Journal ---
    container_titles = crossref_json.get("container-title", [])
    csl["publisher"] = html.unescape(container_titles[0]) if container_titles else ""

    # --- Date ---
    date_parts = None
    if "published-print" in crossref_json:
        date_parts = crossref_json["published-print"].get("date-parts", [[]])[0]
    elif "published-online" in crossref_json:
        date_parts = crossref_json["published-online"].get("date-parts", [[]])[0]

    if date_parts:
        year = str(date_parts[0]) if len(date_parts) > 0 else "0000"
        month = f"{date_parts[1]:02d}" if len(date_parts) > 1 else "01"
        day = f"{date_parts[2]:02d}" if len(date_parts) > 2 else "01"
        csl["date"] = f"{year}-{month}-{day}"
    else:
        csl["date"] = "0000-01-01"

    # --- DOI resolver link ---
    csl["link"] = f"https://doi.org/{crossref_json.get('DOI', '')}"

    # --- Preserve custom fields from original source ---
    if source:
        for key in ["tags", "image"]:
            if key in source:
                csl[key] = source[key]

    return csl


# go through sources
for index, source in enumerate(sources):
    log(f"Source {index + 1} of {len(sources)} - {source.get('id', '-')}", 2)

    cached = find_match(source, citations)
    if cached:
        log("Using existing citation", 3)
        new_citations.append(cached)
    else:
        log("Using Crossref API to generate new citation", 3)
        try:
            doi = source.get("id")
            if not doi:
                raise ValueError("Missing source id")
            doi = doi if doi.startswith("doi:") else f"doi:{doi}"

            resp = requests.get(f"https://api.crossref.org/works/{doi[4:]}")
            if resp.status_code != 200:
                raise RuntimeError(f"Crossref lookup failed for {doi}: {resp.status_code}")
            crossref_data = resp.json()["message"]

            citation = crossref_to_csl(crossref_data, source=source)
            new_citations.append(citation)

        except Exception as e:
            log(f"Failed to generate citation for {doi}: {e}", 3, "")
            exit(1)

log("Exporting citations")

# go through new citations
for citation in new_citations:
    # merge in properties from input source
    citation.update(find_match(citation, sources))

    # ensure date in proper format for correct date sorting
    citation["date"] = clean_date(citation.get("date"))

log(f"Exported {len(new_citations)} citations", 2, "green")

# save new citations
try:
    save_data(config["output"], new_citations)
except Exception as message:
    log(message, 2, "red")
    exit(1)

log("Done!")

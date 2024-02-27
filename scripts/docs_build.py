from mkdocstrings import MkDocsPlugin

# Configure the plugin
plugin = MkDocsPlugin(config_file_path="mkdocs.yml")

plugin.run()

plugin.build()
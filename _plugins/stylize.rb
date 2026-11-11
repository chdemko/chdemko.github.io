require_all "jekyll/filters"
require_all "liquid/standardfilters"


# Declare module of your plugin under Jekyll module
module Jekyll::StylizeFilter

  class Filters
    include Liquid::StandardFilters
  end

  # Each method of the module creates a custom Jekyll filter
  def stylize(input)
    # emphasize filter business logic

    @filters = Filters.new

    input = @context.registers[:site].find_converter_instance(
      Jekyll::Converters::Markdown
    ).convert(input.to_s)

    tags = ["strong", "em", "sub", "sup"]
    for tag in tags
      input = @filters.replace(input, "<" + tag + ">", "__" + tag + "_opened__")
      input = @filters.replace(input, "</" + tag + ">", "__" + tag + "_closed__")
    end
    input = @filters.strip_html(input)
    for tag in tags
      input = @filters.replace(input, "__" + tag + "_opened__", "<" + tag + ">")
      input = @filters.replace(input, "__" + tag + "_closed__", "</" + tag + ">")
    end
    input

  end


end

Liquid::Template.register_filter(Jekyll::StylizeFilter)

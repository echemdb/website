r"""
Implements a `render` filter that renders an object as MarkDown.

EXAMPLES:

The `render` filter renders an element using a specific template::

    >>> from website.macros.render import render
    >>> from io import StringIO
    >>> from astropy.units import Unit

    >>> snippet = StringIO("{{ value | render(template='components/quantity.md') }}")
    >>> render(snippet, value={ 'quantity': 1 * Unit("mol / l") })
    '$1 \\; \\mathrm{M}$'

When no template is given, the filter returns the `markdown` property if
present::

    >>> snippet = StringIO("{{ value | render }}")

    >>> class Value:
    ...     @property
    ...     def markdown(self): return "MarkDown"

    >>> render(snippet, value=Value())
    'MarkDown'

When no template is given, the filter renders the value with the
`markdown_template` if present::

    >>> snippet = StringIO("{{ value | render }}")

    >>> class Value(dict):
    ...     markdown_template = 'components/quantity.md'

    >>> render(snippet, value=Value({ 'quantity': 1 * Unit("mol / l") }))
    '$1 \\; \\mathrm{M}$'

"""

# ********************************************************************
#  This file is part of echemdb.
#
#        Copyright (C) 2021 Albert Engstfeld
#        Copyright (C) 2021-2025 Johannes Hermann
#        Copyright (C) 2021 Julian Rüth
#        Copyright (C) 2021 Nicolas Hörmann
#
#  echemdb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  echemdb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with echemdb. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************


def render(value, template=None):
    r"""
    Return `value` as a MarkDown string.

    Note that this filter might not interact correctly with autoescaping. If
    there are problems, we should revisit the autoescaping advice at
    https://jinja.palletsprojects.com/en/3.0.x/api/#custom-filters.

    EXAMPLES::

        >>> from website.macros.render import render
        >>> from io import StringIO
        >>> from astropy.units import Unit

        >>> snippet = StringIO("{{ value | render(template='components/quantity.md') }}")
        >>> render(snippet, value={ 'quantity': 1 * Unit("A / m^2") })
        '$1 \\; \\mathrm{A\\,m^{-2}}$'

    """
    if template is None:
        if hasattr(value, "markdown"):
            return value.markdown
        if hasattr(value, "markdown_template"):
            template = value.markdown_template
        else:
            raise ValueError(
                "No template specified but value does neither provide a markdown property nor a markdown_template property."
            )
    import website.macros.render

    return website.macros.render.render(template, value=value)


def render_plot(entry):
    r"""
    Return html representation of plotly plot.

    """
    import plotly.graph_objects
    from astropy.units import Unit

    x_label = "E"
    y_label = "j"
    x_label = entry._normalize_field_name(x_label)  # pylint: disable=W0212
    y_label = entry._normalize_field_name(y_label)  # pylint: disable=W0212

    fig = plotly.graph_objects.Figure()

    fig.add_trace(
        plotly.graph_objects.Scatter(
            x=entry.df[x_label],
            y=entry.df[y_label],
            mode="lines",
        )
    )

    x_field = entry.mutable_resource.schema.get_field(x_label).to_dict()
    reference = (
        entry.mutable_resource.schema.get_field(x_label).to_dict().get("reference")
    )
    if reference:
        reference = f" vs. {x_field['reference']}"
    else:
        reference = ""

    fig.update_layout(
        template="simple_white",
        margin={"l": 40, "r": 40, "b": 40, "t": 40},
        xaxis_title=f"<i>{x_label}</i>{reference} / {Unit(entry.field_unit(x_label)).to_string(format='unicode')}",
        yaxis_title=f"<i>{y_label}</i> / {Unit(entry.field_unit(y_label)).to_string(format='unicode')}",
    )

    fig.add_hline(y=0.0, line_width=2)

    x_min = entry.df[x_label].min()
    x_max = entry.df[x_label].max()
    x_padding = (x_max - x_min) * 0.05
    y_min = entry.df[y_label].min()
    y_max = entry.df[y_label].max()
    y_padding = (y_max - y_min) * 0.05

    fig.update_xaxes(
        showline=True, mirror=True, range=(x_min - x_padding, x_max + x_padding)
    )
    fig.update_yaxes(
        showline=True, mirror=True, range=(y_min - y_padding, y_max + y_padding)
    )

    return fig._repr_html_()  # pylint: disable=W0212

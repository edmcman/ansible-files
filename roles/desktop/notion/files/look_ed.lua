-- look_ed.lua drawing engine configuration file for Notion.

if not gr.select_engine("de") then return end

de.reset()

de.defstyle("*", {
    shadow_colour = "#404040",
    highlight_colour = "#707070",
    background_colour = "#3A015C",
    foreground_colour = "#ffffff",
    padding_pixels = 1,
    highlight_pixels = 1,
    shadow_pixels = 1,
    border_style = "elevated",
    font = "xft:Source Sans Pro:size=14",
    text_align = "center",
})

de.defstyle("frame", {
    shadow_colour = "#404040",
    highlight_colour = "#707070",
    padding_colour = "#505050",
    background_colour = "#000000",
    foreground_colour = "#ffffff",
    padding_pixels = 1,
    highlight_pixels = 1,
    shadow_pixels = 1,
})

de.defstyle("tab", {
    font = "xft:Source Sans Pro:size=14",
    de.substyle("active-selected", {
        shadow_colour = "#304050",
        highlight_colour = "#708090",
        background_colour = "#3A015C",
        background_colour = "#8D62A7",
        foreground_colour = "#ffffff",
    }),
    de.substyle("active-unselected", {
        shadow_colour = "#203040",
        highlight_colour = "#607080",
        background_colour = "#3A015C",
        foreground_colour = "#a0a0a0",
    }),
    de.substyle("inactive-selected", {
        shadow_colour = "#404040",
        highlight_colour = "#909090",
        background_colour = "#973E88",
        foreground_colour = "#a0a0a0",
    }),
    de.substyle("inactive-unselected", {
        shadow_colour = "#404040",
        highlight_colour = "#707070",
        background_colour = "#290025",
        foreground_colour = "#a0a0a0",
    }),
    text_align = "center",
})


de.defstyle("input", {
    shadow_colour = "#404040",
    highlight_colour = "#707070",
    background_colour = "#3A015C",
    foreground_colour = "#ffffff",
    padding_pixels = 1,
    highlight_pixels = 1,
    shadow_pixels = 1,
    border_style = "elevated",
    de.substyle("*-cursor", {
        background_colour = "#ffffff",
        foreground_colour = "#000000",
    }),
    de.substyle("*-selection", {
        background_colour = "#8D62A7",
        foreground_colour = "#ffffff",
    }),
})

de.defstyle("input-menu", {
    de.substyle("active", {
        shadow_colour = "#304050",
        highlight_colour = "#708090",
        background_colour = "#506070",
        foreground_colour = "#ffffff",
    }),
})

dopath("lookcommon_emboss")

gr.refresh()


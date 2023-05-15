-- No uso este filtro. Pretitle lo gestiona template partial title-block.html
function Meta(m)
    if m.titlepage then
        local title = pandoc.utils.stringify(m.title)
        local pretitle = pandoc.utils.stringify(m["mnye-book"]["pretitle"])
        m.title = pretitle .. ': ' .. title
    end
    return m
end
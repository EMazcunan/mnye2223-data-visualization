local pre = pandoc.RawBlock('html', '<details> <summary>Solución </summary>')
local post = pandoc.RawBlock('html', '</details>')

function Div (div)
  -- The order of the classes shouldn't matter!
  if div.classes:includes('solution') then
    local content = div.content
    table.insert(content, 1, pre)
    table.insert(content, post)
    return content
  end
  return nil
end
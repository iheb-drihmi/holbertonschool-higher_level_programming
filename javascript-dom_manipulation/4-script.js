document.querySelector('#add_item').onclick = function(){
    let element = document.createElement('li')
    let text = document.createTextNode('item')
    element.appendChild(text)
    document.querySelector('.my_list').appendChild(element)
}
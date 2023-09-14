async function fetchHello() {
    let response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
    const hello = await response.json();

    let hi = document.createElement('p')
    let text = document.createTextNode(hello.hello)
    hi.appendChild(text)
    document.querySelector('#hello').appendChild(hi);
    console.log(hello.hello)

}

fetchHello();
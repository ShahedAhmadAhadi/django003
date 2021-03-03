let input = document.getElementById('search')
let search_str = ''
input.addEventListener("keydown",async function (e) {
    // += e.key
    // console.log(input.value)
    if (e.keyCode > 64 && e.keyCode < 91) {
        search_str += e.key
        fetch(`http://localhost:8000/search/${search_str}`)
                .then(response => response.json()).then(res => console.log(res))
    }
    

 })

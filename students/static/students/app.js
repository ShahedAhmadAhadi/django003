let input = document.getElementById('search')
let show = document.getElementById('search_result')
let search_str = ''
show.innerHTML = ''
input.addEventListener("keyup",async function () {
    let val = input.value
    show.innerHTML = ''

    fetch(`http://localhost:8000/search/${val}`)
        .then(response => response.json()).then(res => {
            for (i in res){
                let li = show.appendChild(document.createElement('li'));
                let span1 = li.appendChild(document.createElement("span"));
                let span2 = li.appendChild(document.createElement('span'));
                span1.appendChild(document.createTextNode(`${res[i]['name']}`))
                span2.appendChild(document.createTextNode(`${res[i]['f/name']}`))
            } 
        })
})

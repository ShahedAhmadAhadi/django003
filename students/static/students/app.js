let input = document.getElementById('search')
let search_str = ''
input.addEventListener("keyup",async function () {
    let val = input.value
    

    fetch(`http://localhost:8000/search/${val}`)
        .then(response => response.json()).then(res => {
            document.getElementById('wrapper').innerHTML = ''
            for (i in res){
                document.getElementById('wrapper').innerHTML += `
                <a href="../home/{{ student.s_roll }}">
                <div class="row">
                    <span> ${res[i]['name']} </span>
                    <span>${res[i]['f/name']}</span>
                </div>
            </a>`
                // let li = show.appendChild(document.createElement('li'));
                // let span1 = li.appendChild(document.createElement("span"));
                // let span2 = li.appendChild(document.createElement('span'));
                // span1.appendChild(document.createTextNode(`${res[i]['name']}`))
                // span2.appendChild(document.createTextNode(`${res[i]['f/name']}`))
            } 
        })
})

let input = document.getElementById('search')
let search_str = ''
input.addEventListener("keydown",async function (e) {
    // += e.key
    // console.log(e.keyCode)
    // if ()
    if (e.keyCode > 64 && e.keyCode < 91 || e.keyCode == 8) {
        search_str += e.key
        if (e.keyCode == 8){
            search_str = search_str.slice(0, search_str.length - 10)
            if (search_str) {
                fetch(`http://localhost:8000/search/${search_str}`)
                    .then(response => response.json()).then(res => {
                        console.log(res)
                    })
            }
        }else{
            // search_str += e.key
            fetch(`http://localhost:8000/search/${search_str}`)
                    .then(response => response.json()).then(res => {
                        console.log(res)
                        // console.log(search_str, 'sdf')
                    })
            
            }
        }
    

 })

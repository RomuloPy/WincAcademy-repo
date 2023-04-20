// API_KEY = eacbfe0afed5b7d5b6056c63dd098adb;

async function getData() {
    try {
        const apiUrl = `https://api.themoviedb.org/3/movie/550?api_key=eacbfe0afed5b7d5b6056c63dd098adb`
        let res = await fetch(apiUrl, {
            method: 'GET'})
            .then(response => response.json())
            .then(data => console.log(data))
        } catch(err) {
            console.log(err)   
        }
}
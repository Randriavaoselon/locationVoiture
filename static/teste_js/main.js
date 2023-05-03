const carsDataBox = document.getElementById('cars-data-box')
const carInput = document.getElementById('cars')

const modelDataBox = document.getElementById('model-data-box')
const carUserInput = document.getElementById('models')

const modelText = document.getElementById("model-text")

$.ajax({
    type: 'GET',
    url: '/car-json/',
    success: function(response){
        console.log(response.data)
        const carsData = response.data
        carsData.map(item => {
            const option = document.createElement('div')
            option.textContent = item.nom
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.nom)
            carsDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }  
})

 carInput.addEventListener('change', e =>{
    console.log(e.target.value)
    const selectedCar = e.target.value

    modelDataBox.innerHTML = ""
    modelText.textContent = "Choisir un model"
    modelText.classList.add("default")

    $.ajax({
        type: 'GET',
        url: `/model-json/${selectedCar}/`,
        success: function(response){
            console.log(response.data)
            const modelUser = response.data
            modelUser.map(item => {
                const option = document.createElement('div')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.nom)
                modelDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }  
    })
 })
function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
}

function reservationPay(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('paiement').getContext('2d');
        var reserve_pay = gera_cor(qtd=12)
        const mychart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Paiements",
                    data: data.data,
                    backgroundColor: reserve_pay[0],
                    borderColor: reserve_pay[1],
                    borderWidth: 1

                }]
            },
        });
    })
}

function location_paiement(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('paie_loc').getContext('2d');
        var loc_paie = gera_cor(qtd=4)
        const mychart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Depense",
                    data: data.data,
                    backgroundColor:loc_paie[0],
                    borderColor:loc_paie[1],
                    borderWidth: 1

                }]
            },
        });
    })

}    
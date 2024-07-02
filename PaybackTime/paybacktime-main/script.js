document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
        })
        .then(data => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('uploadButton').innerText = 'Upload Complete';
                document.getElementById('uploadButton').disabled = true;
            } else {
                alert('File upload failed: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('File upload failed: ' + error);
        });
    }
});

// script.js
document.getElementById('connectButton').addEventListener('click', function() {
    window.location.href = 'secondary_page.html';
});

// Chart.js example initialization
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Year 1', 'Year 2', 'Year 3', 'Year 4'],
        datasets: [{
            label: 'Recommended',
            data: [12, 19, 3, 5],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }, {
            label: 'As Is',
            data: [5, 9, 13, 15],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


// Budget slider functionality
document.getElementById('budgetSlider').addEventListener('input', function(event) {
    const value = event.target.value;
    document.getElementById('budgetValue').innerText = value;
});

// Max Budget input functionality
document.getElementById('maxBudgetInput').addEventListener('input', function(event) {
    const value = event.target.value;
    document.getElementById('maxBudget').innerText = value;

    // Update the max attribute of the budget slider
    document.getElementById('budgetSlider').max = value;
});




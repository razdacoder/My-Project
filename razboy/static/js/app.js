const selected = document.querySelector('.selected')
const selectText = document.querySelector('.selected p')
const selectIcon = document.querySelector('.select-icon')
const optionList = document.querySelector('.option-container')
const options = document.querySelectorAll('.option')

if (selected) {
    selected.addEventListener('click', () => {
        optionList.classList.toggle('active')
        selectIcon.classList.replace('ion-chevron-down', 'ion-chevron-up')
    })
}
if (options) {
    options.forEach(o => {
        o.addEventListener('click', () => {
            selectText.innerHTML = o.querySelector('label').innerHTML;
            optionList.classList.add('active')
        })
    })

}

// const imgLabel = document.querySelectorAll('.imgs-group label')
// const imgInput = document.querySelectorAll('.imgs-group input')

// imgInput.forEach(input => {
//     input.addEventListener('change', (e) => {
//         const el = document.createElement('img')
//         el.src = URL.createObjectURL(input.files[0])
//         el.classList.add('form-img')
//         input.nextElementSibling.innerHTML = el.src
//         el.onload = function () {
//             URL.revokeObjectURL(el.src)
//         }

//     });
// });





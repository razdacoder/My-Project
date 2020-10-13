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
const tabs = document.querySelectorAll('[data-tab-target]')
const tabContent = document.querySelectorAll('.content')
// console.log(tabs)

if (tabs) {
    tabs.forEach(tab => {

        tab.addEventListener('click', () => {
            tab.classList.remove('active')
            const target = document.querySelector(tab.dataset.tabTarget)
            tabContent.forEach(tabcontent => {
                tabcontent.classList.remove('active')
            })
            tabs.forEach(tabcontent => {
                tabcontent.classList.remove('active')
            })
            tab.classList.add('active')
            target.classList.add('active')
        })
    })
}

const state = {}



// const editBtns = document.querySelectorAll('.edit-ad')
// if (editBtns) {
//     editBtns.forEach(btn => {
//         btn.addEventListener('click', (e) => {
//             const btnValue = btn.value
//             console.log(btnValue)
//             fetch(`http://localhost:8000/api/getAd/${btnValue}/`)
//                 .then(response => response.json())
//                 .then(data => {
//                     state.data = data
//                     console.log(state.data.ad)
//                     const editAdPage = `

//                 `
//                     document.querySelector('#edit_ad_page').insertAdjacentElement('afterbegin', editAdPage)

//                 });


//         })
//     })
// }


// const editPic = document.querySelector('.edit-pic')
// if (editPic) {
//     editPic.addEventListener('change', () => {
//         const csrftoken = Cookies.get('csrftoken');
//         axios({
//             method: 'patch',
//             url: `http://127.0.0.1:8000/api/editPic/`,
//             data: {
//                 image: editPic.value,

//             },
//             headers: { 'X-CSRFToken': csrftoken }
//         });
//     })
// }











const openModel = document.querySelectorAll('[data-model-target]');
const closeModel = document.querySelectorAll('[data-close-button]');
const overlay = document.getElementById('overlay');


openModel.forEach(button => {
    button.addEventListener('click', () => {
        const model_part = document.querySelector(button.dataset.modelTarget)
        openModel(model_part)
    })
});

closeModel.forEach(button => {
    button.addEventListener('click', () => {
        const model_part = button.closest('.modal')
        closeModel(model_part)
    })
});

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.model')
    modals.forEach(modal => {
        closeModel(modal)
    })
});

function openModel(model_part) {
    if (model_part == null) return
    model_part.classList.add('active')
    overlay.classList.add('active')
}

function closeModel(model_part) {
    if (model_part == null) return
    model_part.classList.remove('active')
    overlay.classList.remove('active')
}; 
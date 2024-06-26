function calculate(data) {
    console.log(data)
}

document.querySelector(".container-hora-extra").addEventListener("submit", (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target).entries());
    let salario = document.getElementById("salario");
    console.log(salario);
    console.log(data);
})

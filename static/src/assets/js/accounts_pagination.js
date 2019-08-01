(() => {
    function copyToClipboard(element) {
        const input = document.createElement("input");
        input.style = "position: absolute; left: -1000px; top: -1000px";
        input.value = element.dataset.password;
        document.body.appendChild(input);
        input.select();
        document.execCommand("copy");
        document.body.removeChild(input);
    }

    document.querySelectorAll('[data-password]').forEach(el => {
        el.onclick = _ => copyToClipboard(el)
    })
})()
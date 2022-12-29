const messageTextInput = document.getElementById('messageText');
const commandModeInput = document.getElementById('commandMode');
const statusBar = document.getElementById('statusBar');

commandModeInput.focus();

document.addEventListener('keyup', event => {
    if (event.key === "i") { messageTextInput.focus(); setMode("insert");}
    if (event.key === "c") { messageTextInput.focus(); messageTextInput.value=""; setMode("insert")}
    if (event.key === "Escape") { commandModeInput.focus(); setMode("command"); }
})
function setMode(mode) {
    mode = mode;
    statusBar.querySelector('.mode').textContent = `---${mode}---`;
    commandModeInput.value = '';
}
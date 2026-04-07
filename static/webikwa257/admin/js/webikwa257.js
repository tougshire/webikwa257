window.addEventListener("load", function(e) {
  document.getElementById("page-edit-form").addEventListener("click", function(e) {
    if(e.target.className=="copy_image_url") {
        e.preventDefault()
        el_copy = document.createElement("textarea")
        document.body.appendChild(el_copy)
        el_copy.innerHTML=e.target.previousSibling.previousSibling.innerHTML
        el_copy.select()
        document.execCommand("copy")
        document.body.removeChild(el_copy)
    }
  })
})

function confirElimina(id) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: '¿Estas seguro ?',
        text: "No podras recuperar los datos eliminados",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'si, eliminar!',
        cancelButtonText: 'Cancelar',
        reverseButtons: true
    }).then((result) => {
        if (result.value) {
            // redirigir
            window.location.href = "/elimina/" + id + "/";

        }

    })
}

/* {% url 'elimina' p.id %} */
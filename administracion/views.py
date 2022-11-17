from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import UserForm, UpdateUserForm, PasswordChangeForm, NuevaFabrica, NuevaCategoria, NuevoProducto
from tienda.models import Fabrica, Producto, Usuario, Categoria, Pedido, Detalle


@login_required(login_url='/acceder/')
def fabricas(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    f = Fabrica.objects.all()
    context = {
        'section': 'fabricas',
        'fabricas': f,
        'estados': {
            'A': 'Activo',
            'I': 'Inactivo',
        }
    }
    return render(request, 'administracion/fabricas.html', context)


@login_required(login_url='/acceder/')
def registrar_fabrica(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = NuevaFabrica()
    if (request.method == 'POST'):
        form = NuevaFabrica(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/administracion/fabricas/')
    context = {
        'section': 'fabricas.registrar',
        'form': form,
        'estados': {
            'A': 'Activo',
            'I': 'Inactivo',
        }
    }
    return render(request, 'administracion/fabricas.registrar.html', context)


@login_required(login_url='/acceder/')
def activar_fabrica(request, accion, id):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    f = Fabrica.objects.filter(id=id)
    if f:
        f = f[0]
        f.estado = 'A' if accion == 'activar' else 'I' if accion == 'desactivar' else f.estado
        f.save()
        messages.success(request, '¡La fábrica %s se ha %sdo exitosamente!' % (f, accion[:-1]))
    else:
        messages.error(request, 'No se encontró la fábrica.', extra_tags='danger')
    return redirect('/administracion/fabricas/')


@login_required(login_url='/acceder/')
def categorias(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    c = Categoria.objects.all()
    context = {
        'section': 'categorias',
        'categorias': c,
        'estados': {
            'A': 'Activo',
            'I': 'Inactivo',
        }
    }
    return render(request, 'administracion/categorias.html', context)


@login_required(login_url='/acceder/')
def registrar_categoria(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = NuevaCategoria()
    if (request.method == 'POST'):
        form = NuevaCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/administracion/categorias/')
    context = {
        'section': 'categorias.registrar',
        'form': form,
        'estados': {
            'A': 'Activo',
            'I': 'Inactivo',
        }
    }
    return render(request, 'administracion/categorias.registrar.html', context)


@login_required(login_url='/acceder/')
def activar_categoria(request, accion, id):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    c = Categoria.objects.filter(id=id)
    if c:
        c = c[0]
        c.estado = 'A' if accion == 'activar' else 'I' if accion == 'desactivar' else c.estado
        c.save()
        messages.success(request, '¡La cateogoría %s se ha %sdo exitosamente!' % (c, accion[:-1]))
    else:
        messages.error(request, 'No se encontró la cateogoría.', extra_tags='danger')
    return redirect('/administracion/categorias/')


@login_required(login_url='/acceder/')
def inventario(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    p = Producto.objects.all()
    context = {
        'section': 'inventario',
        'productos': p
    }
    return render(request, 'administracion/inventario.html', context)


@login_required(login_url='/acceder/')
def registrar_producto(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = NuevoProducto()
    c = Categoria.objects.filter(estado='A')
    f = Fabrica.objects.filter(estado='A')
    if (request.method == 'POST'):
        form = NuevoProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/administracion/inventario/')
    context = {
        'section': 'productos.registrar',
        'form': form,
        'categorias': c,
        'fabricas': f,
        'estados': {
            'A': 'Activo',
            'I': 'Inactivo',
        }
    }
    return render(request, 'administracion/productos.registrar.html', context)


@login_required(login_url='/acceder/')
def editar_producto(request, id):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = NuevoProducto()
    p = Producto.objects.filter(id=id)
    if not p:
        messages.error(request, 'No se encontró el producto.', extra_tags='danger')
        return redirect('/administracion/inventario/')
    p = p[0]
    c = Categoria.objects.filter(estado='A')
    f = Fabrica.objects.filter(estado='A')
    if (request.method == 'POST'):
        form = NuevoProducto(request.POST)
        if form.is_valid():
            p.nombre = form.cleaned_data.get('nombre')
            p.descripcion = form.cleaned_data.get('descripcion')
            p.precio = form.cleaned_data.get('precio')
            p.precio_pedido = form.cleaned_data.get('precio_pedido')
            p.imagen = form.cleaned_data.get('imagen')
            p.estado = form.cleaned_data.get('estado')
            p.categoria = form.cleaned_data.get('categoria')
            p.fabrica = form.cleaned_data.get('fabrica')
            p.save()
            return redirect('/administracion/inventario/')
    context = {
        'section': 'productos',
        'form': form,
        'producto': p,
        'categorias': c,
        'fabricas': f,
        'estados': {
            'A': 'Activo',
            'I': 'Inactivo',
        }
    }
    return render(request, 'administracion/productos.editar.html', context)


@login_required(login_url='/acceder/')
def activar_productos(request, accion, id):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    p = Producto.objects.filter(id=id)
    if p:
        p = p[0]
        p.estado = 'A' if accion == 'activar' else 'I' if accion == 'desactivar' else p.estado
        p.save()
        messages.success(request, '¡El producto %s se ha %sdo exitosamente!' % (p, accion[:-1]))
    else:
        messages.error(request, 'No se encontró el producto.', extra_tags='danger')
    return redirect('/administracion/inventario/')


@login_required(login_url='/acceder/')
def pedidos(request):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    p_ingresados = Pedido.objects.filter(estado='I')
    p_cancelados = Pedido.objects.filter(estado='C')
    p_recibidos = Pedido.objects.filter(estado='R')
    context = {
        'section': 'pedidos',
        'pedidos': [
            {'listado': p_ingresados, 'titulo': 'ingresados'},
            {'listado': p_recibidos, 'titulo': 'recibidos'},
            {'listado': p_cancelados, 'titulo': 'cancelados'},
        ]
    }
    return render(request, 'administracion/pedidos.html', context)


@login_required(login_url='/acceder/')
def registrar_pedido(request, fabrica=None):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    p = Producto.objects.filter(fabrica=fabrica) if fabrica else None
    f = Fabrica.objects.get(id=fabrica) if fabrica else Fabrica.objects.filter(estado='A')
    if request.method == 'POST':
        try:
            total, detalle_pedido = 0, []
            for producto in p:
                unidades = int(request.POST.get('unidades%d' % producto.id, 0))
                if unidades > 0:
                    total += producto.precio_pedido * unidades
                    detalle_pedido.append({
                        'quantity': unidades,
                        'subtotal': producto.precio_pedido * unidades,
                        'product': producto
                    })
            # crear pedido
            if detalle_pedido:
                pedido = Pedido(total=total, usuario=request.user)
                pedido.save()
                for detalle in detalle_pedido:
                    d = Detalle(
                        cantidad = detalle['quantity'],
                        total = detalle['subtotal'],
                        pedido = pedido,
                        producto = detalle['product']
                    )
                    print([d])
                    d.save()
                return redirect('/administracion/pedidos/')
            else:
                messages.error(request, 'Debe ingresar al menos una unidad para crear el pedido. Ingrese el pedido nuevamente.', extra_tags='danger')
        except Exception:
            messages.error(request, 'Hubo un problema al procesar el pedido. Ingrese el pedido nuevamente.', extra_tags='danger')
        
    print(f)
    context = {
        'section': 'pedidos.registrar',
        'fabricas': f,
        'productos': p,
        'estados': {
            'I': 'Ingresado',
            'C': 'Cancelado',
            'R': 'Recibido',
        }
    }
    return render(request, 'administracion/pedidos.registrar.html', context)


@login_required(login_url='/acceder/')
def detalle_pedido(request, id):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    p = Pedido.objects.filter(id=id)
    if not p:
        messages.error(request, 'No se encontró el pedido.', extra_tags='danger')
        return redirect('/administracion/pedidos/')
    p = p[0]
    d = Detalle.objects.filter(pedido=p)
    context = {
        'section': 'pedidos',
        'pedido': p,
        'detalles': d,
        'estados': {
            'I': 'Ingresado',
            'C': 'Cancelado',
            'R': 'Recibido',
        }
    }
    return render(request, 'administracion/pedidos.detalle.html', context)


@login_required(login_url='/acceder/')
def procesar_pedido(request, accion, id):
    if request.user.tipo not in ('A', 'E'):
        messages.error(request, 'Acceso sólo para empleados y administradores.', extra_tags='danger')
        return redirect('/perfil/')
    p = Pedido.objects.filter(id=id)
    if not p:
        messages.error(request, 'No se encontró el pedido.', extra_tags='danger')
        return redirect('/administracion/pedidos/')
    p = p[0]
    if p.estado == 'I':
        if accion == 'cancelar':
            p.estado = 'C'
        elif accion == 'recibir':
            p.estado = 'R'
            detalles = Detalle.objects.filter(pedido=p)
            for d in detalles:
                prod = d.producto
                prod.unidades += d.cantidad
                prod.save()
        p.save()
        messages.success(request, '¡El %s se ha %sdo exitosamente!' % (p, accion[:-1]))
    else:
        messages.error(request, 'No se puede cambiar el estado del pedido si no está en estado Ingresado.', extra_tags='danger')
    return redirect('/administracion/pedidos/')


@login_required(login_url='/acceder/')
def usuarios(request):
    if request.user.tipo != 'A':
        messages.error(request, 'Acceso sólo para administradores.', extra_tags='danger')
        return redirect('/perfil/')
    u = Usuario.objects.filter(id__gt=1)
    context = {
        'section': 'usuarios',
        'usuarios': u,
        'estados': {
            'C': 'Cliente',
            'E': 'Empleado',
            'A': 'Administrador',
        }
    }
    return render(request, 'administracion/usuarios.html', context)


@login_required(login_url='/acceder/')
def registrar_usuario(request):
    if request.user.tipo != 'A':
        messages.error(request, 'Acceso sólo para administradores.', extra_tags='danger')
        return redirect('/perfil/')
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('first_name')
            messages.success(request, 'Usuario %s registrado exitosamente.' % name)
            form.save()
            return redirect('/administracion/usuarios/')
    context = {
        'section': 'usuarios.registrar',
        'form': form,
        'estados': {
            'C': 'Cliente',
            'E': 'Empleado',
            'A': 'Administrador',
        }
    }
    return render(request, 'administracion/usuarios.registrar.html', context)


@login_required(login_url='/acceder/')
def editar_usuario(request, id):
    if request.user.tipo != 'A':
        messages.error(request, 'Acceso sólo para administradores.', extra_tags='danger')
        return redirect('/perfil/')
    u = Usuario.objects.filter(id=id)
    if not u:
        messages.error(request, 'No se encontró el usuario.', extra_tags='danger')
        return redirect('/administracion/usuarios/')
    u = u[0]
    form = UpdateUserForm()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.tipo = form.cleaned_data.get('tipo')
            form.save(commit=False)
            u.save()
            messages.success(request, '¡El perfil del usuario %s se ha actualizado exitosamente!' % u)
            return redirect('/administracion/usuarios/')
        else:
            messages.error(request, 'Hubo un error al actualizar el perfil del usuario ' + u, extra_tags='danger')
    context = {
        'section': 'usuarios',
        'usuario': u,
        'form': form,
        'estados': {
            'C': 'Cliente',
            'E': 'Empleado',
            'A': 'Administrador',
        }
    }
    return render(request, 'administracion/usuarios.editar.html', context)


@login_required(login_url='/acceder/')
def editar_contrasena_usuario(request, id):
    if request.user.tipo != 'A':
        messages.error(request, 'Acceso sólo para administradores.', extra_tags='danger')
        return redirect('/perfil/')
    u = Usuario.objects.filter(id=id)
    if not u:
        messages.error(request, 'No se encontró el usuario.', extra_tags='danger')
        return redirect('/administracion/usuarios/')
    u = u[0]
    form = PasswordChangeForm()
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid() and form.cleaned_data.get('new_password1') == form.cleaned_data.get('new_password2'):
            u.set_password(form.cleaned_data.get('new_password1'))
            u.save()
            if u.id == request.user.id:
                update_session_auth_hash(request, u)
            messages.success(request, '¡La contraseña se ha actualizado exitosamente.')
            return redirect('/administracion/usuarios/')
        else:
            messages.error(request, 'Hubo un error al actualizar contraseña.', extra_tags='danger')
    context = {
        'section': 'usuarios',
        'usuario': u,
        'form': form
    }
    return render(request, 'administracion/usuarios.contrasena.html', context)


@login_required(login_url='/acceder/')
def activar_usuario(request, accion, id):
    if request.user.tipo != 'A':
        messages.error(request, 'Acceso sólo para administradores.', extra_tags='danger')
        return redirect('/perfil/')
    u = Usuario.objects.filter(id=id)
    if u:
        u = u[0]
        u.is_active = False if accion == 'deshabilitar' else True if accion == 'habilitar' else u.is_active
        u.save()
        messages.success(request, '¡El usuario %s se ha %sdo exitosamente!' % (u, accion[:-1]))
    else:
        messages.error(request, 'No se encontró el usuario.', extra_tags='danger')
    return redirect('/administracion/usuarios/')

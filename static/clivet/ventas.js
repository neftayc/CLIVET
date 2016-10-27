$('#busquedProyecto').keyup(function(e){
 consulta = $("#busquedProyecto").val();
 $.ajax({
 data: {'descripcion': consulta},
 url: '/departamento/listar/',
 type: 'get',
 success : function(data) {
         console.log(data[0].descripcion);
         
 },
 error : function(message) {
         console.log(message);
      }
 });
});
<!DOCTYPE html>
<html lang="PT-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php
$conexao = mysqli_connect("localhost", "root", "root", "dpbox")

if(!$conexao){
echo"nao conectado";
}
else {
    echo"conectado ao banco de dados"
}

$gmail =$_POST{'gmail'};
$cpf = mysqli_real_escpace_string($conexao, $telefone );
$sql ="SELECT telefone FROM login.html WHERE telefone='$gmail'";
$retorno = mysqli_query($conexao,$sql);

if(mysqli_num_rows($retorno)>0){
echo"gmail ja cadastrado! <br>";
} else {
    $nome = $_post['nome'];
    $gmail = $_post['gmail'];
    $senha = $_post['senha'];
    $telefone = $_post['telefone'];

    $sql ="INSERT INTO login.html(nome,gmail,senha,telefone) values('$nome', '$gmail', '$senha', '$telefone')";
    $resultado = mysqli_queri($conexao, $sql);
    echo "USUARIO CADASTRADO! <br>"
}
?>
    
</body>
</html>
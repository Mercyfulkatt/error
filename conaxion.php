<?php 

#aqui
/***varias lineas */
class conexion {
    public $base = "";
    public $con = "";
    public $user = "";
    public $pass = "";
    
    public __constructor ($con,$bas,$user,$pas){
        $this->base=$base;
        $this->con=$con;
        $this->user=$user;
        $this->pass=$pass;

    }

    public conectar (){
        try{
            $CONECTAR='PDO'
        } catch PDO($e->exeception) {
            echo "$e->getMessage()";
        }
    }
}

?>

import React from "react";
 export function Info(props){
    return(
        <>
        <h2>Salut {props.nombre} {props.personne.nom}  {props.personne.prenom} {props.personne.age}</h2> <hr></hr>
        </>
    )
 }
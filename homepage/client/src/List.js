import  React from 'react'
import data from "./results.json"

function List(props) {
    if (data.length){
        return (
            <ul>
                {data.map((item) => (
                    <tr key={item.id}>
                    <tr><h5><a target ="_blank" href={item.url}>{item.title}</a></h5></tr>
                    <tr><font size="2">{item.description}</font></tr>
                    <br/>
                </tr>
                ))}
            </ul>
        )
}
    else return "";
}


export default List

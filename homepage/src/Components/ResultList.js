import { React } from 'react'
import data from "./SearchData.json"

function ResultList(props) {
    const filteredResults = data.filter((element) => {
        if (props.input === '') {
        }
// return matching results
        else {
            return element.text.toLowerCase().includes(props.input)
        }
    })
    return (
        <ul>
            {filteredResults.map((item) => (
                <li key={item.id}><a target="_blank" href={item.url}>{item.text}</a></li>
            ))}
        </ul>
    )
}

export default ResultList

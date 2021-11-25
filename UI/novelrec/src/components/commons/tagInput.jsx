import React from 'react';


const TagInput  = (props) => {
    const [ tags, setTags ] = React.useState(props.tags)
    const  placeholder  = props.placeholder
    const addTag = (e) => {
        if(e.key === 'Enter') {
            if (e.target.value.length > 0){
                setTags([...tags, e.target.value])
                e.target.value = '';
            }
            }
        }

    const removeTag = removedTag => {
        const newTags = tags.filter(tag => tag !== removedTag)
        setTags(newTags)
    }

    return ( 
        <React.Fragment>
            
            <div className="tag-container">
                <ul id="tags">
               {tags.map((tag, index) => {
                   return (
                       <li key={index} className="tag">
                           <span className="tag-title" >{tag}</span>
                           <span className="tag-close-icon" onClick={() => removeTag(tag)}>x</span>
                        </li>
                   );
               })}
               </ul>
               <input placeholder={placeholder}  onKeyDown={addTag} />

            </div>

        </React.Fragment>
     );
}
 
export default TagInput ;
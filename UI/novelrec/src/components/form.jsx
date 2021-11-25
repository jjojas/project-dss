import React from 'react';

class Form extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        data: {
            books: [''],
            tags: ['']
        }
    }

}

    

    handleSubmit = e => {

        e.preventDefault();

        this.doSubmit();

    }

    addBook = e => {
        if(e.key === 'Enter') {
            if (e.target.value.length > 0){
                const newbooks = [...this.state.data.books, e.target.value]
                let data = this.state.data;
                data["books"] = newbooks;
                this.setState({data});
                e.target.value = '';
            }
            }
        }

    addTag = e => {
        if(e.key === 'Enter') {
            if (e.target.value.length > 0){
                const newtags = [...this.state.data.tags, e.target.value]
                let data = this.state.data;
                data["tags"] = newtags;
                this.setState({data});
                e.target.value = '';
            }
            }
        }
    
    removeBook = removedBook => {
        let data = this.state.data
        data["books"] = data.books.filter(book => book !== removedBook)
        this.setState({data});
    }

    removeTag = removedTag => {
        let data = this.state.data
        data["tags"]=data.tags.filter(tag => tag !== removedTag)
        this.setState({data});
    }

    renderInputBook(){
        const books = this.state.data.books;
        return (<div className="tag-container">
        <ul id="tags">
       {books.map((book, index) => {
           return (
               <li key={index} className="tag">
                   <span className="tag-title" >{book}</span>
                   <span className="tag-close-icon" onClick={() => this.removeBook(book)}>x</span>
                </li>
           );
       })}
       </ul>
       <input placeholder="Ketikkan judul novel"  onKeyDown={this.addBook}/>
    </div>
    );
    } 

    renderInputTags(){
        const tags = this.state.data.tags;
        return (<div className="tag-container">
        <ul id="tags">
       {tags.map((tag, index) => {
           return (
               <li key={index} className="tag">
                   <span className="tag-title" >{tag}</span>
                   <span className="tag-close-icon" onClick={() => this.removeTag(tag)}>x</span>
                </li>
           );
       })}
       </ul>
       <input placeholder="Ketikkan genre novel"  onKeyDown={this.addTag}/>
    </div>
    );
    } 





}
 
export default Form;
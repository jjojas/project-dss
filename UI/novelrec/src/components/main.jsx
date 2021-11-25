import React from 'react';
import Form from './form';
import Button from '@mui/material/Button';
import { getBookId } from '../services/getBookIdService';
import { recommend } from '../services/recommendationService';


class Main extends Form {
    constructor(props) {
        super(props);
        this.state = {
            data: {
                books: [''],
                tags: ['']
            }
        }
    
    }




    doSubmit = async () => {
        // call API server  
        try {
        const booksId = getBookId(this.state.data.books)  
        const { data: bookList} = await recommend(this.state.data.tags, booksId);
        sessionStorage.setItem('bookList', bookList);
        this.props.history.push('/successPage');
        }
        catch (e) {
            alert(e);
        }
        
    }


    render() { 
        return (
        <div>
            <form onSubmit={this.handleSubmit}>
            `   <h1 >Sistem Rekomendasi Novel</h1>
                <h3 >Masukkan judul novel yang pernah dibaca :</h3>
                {this.renderInputBook()}
                <h3 >Masukkan genre novel yang diingingkan :</h3>
                {this.renderInputTags()}
                <button id="tombol" variant="contained">Cari rekomendasi</button>
            </form>
        </div>
        )
        ;
    }
}

 
export default Main;
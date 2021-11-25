import React from 'react';
import TagInput from './commons/tagInput';
import Button from '@mui/material/Button';


class Main  extends React.Component {


    state = {
        data: {
            books: [""],
            tags: [""]
        }
    }

    handleSubmit = e => {
        e.preventDefault();
    }
    state = {
        data:{
            books:[this.state.data.books],
            tags:[this.state.data.tags]
        }
    }
    render() { 
        return (
        <div>
            <h1 >Sistem Rekomendasi Novel</h1>
            <form onSubmit={this.handleSubmit}>
                <h3 >Masukkan judul novel yang pernah dibaca :</h3>
                <TagInput tags={this.state.data.books} placeholder={"ketikkan judul novel"}  />
                <h3 >Masukkan genre novel yang diingingkan :</h3>
                <TagInput tags={this.state.data.tags} placeholder={"Ketikkan genre novel"} />
                <Button id="tombol" variant="contained">Cari rekomendasi</Button>
            </form>
        </div>
        )
        ;
    }
}
 
export default Main;
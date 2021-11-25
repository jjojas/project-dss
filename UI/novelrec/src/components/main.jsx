import React from 'react';
import TagInput from './commons/tagInput';
import Button from '@mui/material/Button';


class Main  extends React.Component {
    state = {
        data: {
            books: [],
            tags: []
        }
    }

    handleSubmit = e => {
        e.preventDefault();
    }

    handleInput(x){
        const newdata = this.state.data
        newdata["books"] = x
        this.setState({
            data : newdata
        });
        alert(this.state.data.books);
      }

    render() { 
        return (
        <div>
            <h1 >Sistem Rekomendasi Novel</h1>
            <form onSubmit={this.handleSubmit}>
                <h3 >Masukkan judul novel yang pernah dibaca :</h3>
                <TagInput tags={["Harry potter"]} placeholder={"ketikkan judul novel"} getInput={this.handleInput} />
                <h3 >Masukkan genre novel yang diingingkan :</h3>
                <TagInput tags={[]} placeholder={"Ketikkan genre novel"} />
                <Button id="tombol" variant="contained">Cari rekomendasi</Button>
            </form>
        </div>
        );
    }
}
 
export default Main;
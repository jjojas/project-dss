import React from 'react';
import TagInput from './commons/tagInput';
import Button from '@mui/material/Button';


class Main  extends React.Component {
    state = {
        judulNovel : [],
        genreNovel : []
    }

    handleSubmit = () => {

        console.log(this.state.genreNovel);
    }


    render() { 
        return (
        <div>
            <h1 >Sistem Rekomendasi Novel</h1>
            <form>
                <h3 >Masukkan judul novel yang pernah dibaca :</h3>
                <TagInput tags={[]} placeholder={"ketikkan judul novel"} />
                <h3 >Masukkan genre novel yang diingingkan :</h3>
                <TagInput tags={[]} placeholder={"Ketikkan genre novel"} />
                <button>Cari rekomendasi</button>
            </form>
        </div>
        );
    }
}
 
export default Main;
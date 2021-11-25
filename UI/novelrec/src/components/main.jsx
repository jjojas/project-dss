import React from 'react';
import Form from './form';
import Button from '@mui/material/Button';


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
        await loginService.login(this.state.data);
        this.props.history.push('/successPage');
        }
        catch (e) {
            alert(e);
        }
        
       console.log(this.state.data);
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
                <Button id="tombol" variant="contained">Cari rekomendasi</Button>
            </form>
        </div>
        );
    }
}

 
export default Main;
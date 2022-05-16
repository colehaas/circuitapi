import React from 'react';
import axios from 'axios';

const baseURL = "/fullstudy/"


export default class App extends React.Component {
  state = {
    name: ''
  }

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const user = {
        withCredentials: true,
        xsrfHeaderName: 'X-CSRFToken',
        xsrfCookieName: 'csrftoken',
        name: this.state.name,
    };

    axios.post(baseURL, { user })
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Expr:
            <input type="text" name="name" onChange={this.handleChange} />
          </label>
          <button type="submit">Add</button>
        </form>
      </div>
    )
  }
}
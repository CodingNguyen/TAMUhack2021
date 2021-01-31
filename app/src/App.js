import AppBar from '@material-ui/core/AppBar';
import Typography from '@material-ui/core/Typography';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <AppBar style={{backgroundColor: "#232323"}}>
          <Typography>
          <h1 align="center">Howdy!</h1>
          </Typography>
        </AppBar>
      </header>
    </div>
  );
}

export default App;

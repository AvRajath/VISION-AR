const express = require('express');
const app = express();
app.use(express.json());
app.get('/', (req, res) => {
    res.send(iotdata);
})

let iotdata = [
	{
		"id": 0,
		"name": "Device-1",
		"status": "OFF"
	},
	{
		"id": 1,
		"name": "Device-2",
		"status": "OFF"
    },
    {
		"id": 2,
		"name": "Device-3",
		"status": "OFF"
    },
    {
		"id": 3,
		"name": "Device-4",
		"status": "OFF"
	}
];

app.post('/', (req, res) => {
	let newiotdata = {
		"id": req.body.id,
		"name": req.body.name,
		"status": req.body.status
    };
    if(newiotdata['name'] != 'test')
    {
        if(newiotdata['id'] == 0)
        {
            iotdata[0]['status']=newiotdata['status']
        }
        if(newiotdata['id'] == 1)
        {
            iotdata[1]['status']=newiotdata['status']
        }
        if(newiotdata['id'] == 2)
        {
            iotdata[2]['status']=newiotdata['status']
        }
        if(newiotdata['id'] == 3)
        {
            iotdata[3]['status']=newiotdata['status']
        }
        console.log(req.body);
        
    }
    res.send(iotdata);
});
const port = process.env.PORT || 1337;
app.listen(port, () => console.log('started and listening. %d', port));


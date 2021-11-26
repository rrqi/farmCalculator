const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = 'bex.';

const fs = require('fs');

const { disconnect, title } = require('process');

const Enmap = require('enmap');

const osu = require('node-osu');

const osuApi = new osu.Api('Spt1wjMN9BiFMoQlxKSm2TSWxClOGqGEFkxE7FyY', {
    notFoundAsError: true,
    completeScores: false,
    parseNumeric: false,
});





client.commands = new Enmap();

fs.readdir("./events/", (err, files) => {
    if (err) return console.error(err);
    files.forEach( async file => {
        if (!file.endsWith(".js")) return;
        const event = require(`./events/${file}`);
        let eventName = file.split(".")[0];
        client.on(eventName, event.bind(null, client));
        delete require.cache[require.resolve(`./events/${file}`)];
    });
});

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command)
}



client.embed = (title, description = '', image = '', fields = undefined ) =>{

    return {embed:{
    title: title,
    url: `https://www.youtube.com/watch?v=40qJapBsOp4`,
    image: {url: image},
    color: '#ff99fc',
    description: description,
    fields: fields
    
}}}

client.sendembed = (channel, title, description, image = '', fields = undefined ) =>{
    
    channel.send(
        client.embed(title, description, image, fields)
        )
    
}
client.on('guildMemberAdd', member =>{
    const channel = member.guild.channels.cache.find(ch => ch.id === '701495107932651522');

    client.messagelist = require('./komodo.json');

    const index = Math.floor( Math.random() * client.messagelist.length );

    const content = client.messagelist[ index ];

    // Do nothing if the channel wasn't found on this server
    if (!channel) {
        console.log('channel not found')
        return;
    }
    // Send the message, mentioning the member
    channel.send(`Welcome to the server, ${member}, ${content}`);
})





client.on('message', message => {
    if(message.author.bot) return;
    

    client.messagelist = require('./komodo.json');

    //const poggers = require('./poggers.json');
    
    index = Math.floor( Math.random() * client.messagelist.length );
    
    const content = client.messagelist[ index ];

    if(message.channel.type == "dm"){
        client.users.fetch("221902402905833482").then((user)=>{
            user.send(message.author.username + ": " + message.content)
            user.send("bexbot to "+message.author.username+": "+content)
            message.channel.send(content)
        })
        
    }
    var store = true;

    function prefixdisable(prefix){
        if(message.content.toLowerCase().startsWith(prefix)){
            store = false;
            return;
        }
    }

    if(message.author.id == 754542036862107728)return;

    prefixdisable('$');
    prefixdisable('w.');
    prefixdisable('>');
    prefixdisable('bex.');
    prefixdisable('!');
    prefixdisable('p!')
    prefixdisable('t!')
    prefixdisable('s?');
    

    if(store === true && message.content){
        if (!message.content.includes('bex') && !message.content.startsWith("bex.")) {
            client.messagelist.push(message.content);
            fs.writeFile('./komodo.json', JSON.stringify(client.messagelist), err => {if (err) console.error(error)});
    }}
    const msg = message.content.trim(' ').toLowerCase();
    
    if (msg.includes('bex') && !msg.startsWith("bex.")) {
        //message.channel.send('it is I.');
        if(!message.channel.type == "dm"){
            if(message.channel.permissionsFor(message.guild.me).any("SEND_MESSAGES", true) == true){
                

                message.channel.send(client.messagelist[ index ])

                console.log(new Date()+': summon->'+message.channel.name+', '+message.author.username)
            }
        }
        else {
            message.channel.send(client.messagelist[ index ])

            console.log(new Date()+': summon->'+message.channel.name+', '+message.author.username)
        }
    } 
    
    

    //pog
    if(msg.includes('pog')){
            //message.react(client.emojis.resolve("🧑‍🌾"))   
            //message.react("🧑‍🌾")
            if(message.channel.permissionsFor(message.guild.me).any("SEND_MESSAGES", true) == true && message.channel.nsfw == false){
                //message.channel.send('pog')
                poggers = require("./poggers.json")
                index = Math.floor(Math.random()*poggers.length)
                message.channel.send(poggers[index]);
    }}

    if(message.content.includes('arnold')){
        if(message.channel.permissionsFor(message.guild.me).any("SEND_MESSAGES", true) == true && message.channel.nsfw == false){
            //message.channel.send('pog')
            workout = require("./workout.json")
            index = Math.floor(Math.random()*workout.length)
            message.author.send(workout[index]);
    }}

    if(msg.startsWith("bex.")){
        var name =  message.author.username
        console.log(name+"->"+msg)
    }
});

const komodo = require('./komodo.json')
console.log(komodo.length)




































































































































































client.login('##########################################');
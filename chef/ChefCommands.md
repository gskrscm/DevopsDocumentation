## Knife configuration after chefdk installation. 
- Create .chef folder
- copy pem file to .chef folder 
- create knife.rb
```
current_dir = File.dirname(__FILE__)
log_level :info
log_location STDOUT
node_name "chefadmin"
client_key "#{current_dir}/chefadmin.pem"
chef_server_url "https://chef-server/organizations/mycompany"
cookbook_path ["#{current_dir}/../cookbooks"]
knife[:editor] = "vim"
```
- knife ssl fetch 

## knife commands

1. Create a cookbook.
<pre>Chef generate `repo`</pre>
<pre>knife cookbook create `cookbookname`</pre>
2. Add dependencies to the cookbook.

 we need to add in metadata file `depends cookbooname` , then run berks command `berks install` it will download the dependencies to user/.bershelf/cookbooks

3. To upload cookbook
<pre> knife cookbook upload `cookbookname` </pre>
<pre> berks upload --no-ssl-verify </pre>

4. Set runlist for the server.
<pre>knife node list</pre>
<pre>knife node run_list add nodename 'role[cookbookname]' </pre>

5. Run cookbook.

    `chef-client` on the server.

6.  To run cookbook from workstation

`knife ssh "tags:<tag name> AND platform:<operating systme> AND chef_environment:<environment>" -x "username" -P "password" "sudo chef-client -o recipe[cookbookname]"`

7. To edit chef node parameter. 

`knife node edit <node name>`

----------------------------------------------


 Creating a role
   - add runlist

  To see list of roles
   `knife role list`

 To add the role
 `kinfe role from_file filename`

 `knife role show cookbookname`

 `knife cookbook list`



 `knife node list`

 `knife node run_list add nodename 'role[cookbookname]'`


 then run chef-client on the server




## Databags
Create data bag
`knife data bag create <data bag name>`
`knife data bag from file <data bag name> <json file>.json`

To show data bags available
`knife data bag list`

To show data bags
`knife data bag show <data bag name> `

Usage

user = data_bag_item('databag name', 'databag id');

user['id']

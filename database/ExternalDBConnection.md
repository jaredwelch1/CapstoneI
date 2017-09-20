### Allowing remote access to PostgreSQL db
- Change listen address in file `/etc/postgresql/9.5/main/postgresql.conf` from `#listen_addresses = 'localhost'` to `listen_addresses = '*'`
- Add `host all all 0.0.0.0/0 md5` to the end of `/etc/postgresql/9.5/main/pg_hba.conf` 
- Restart postgresql server: `postgresql restart`
- To login via SSH: `psql -h ec2-35-163-99-253.us-west-2.compute.amazonaws.com -p 9000 -U postgres`
import socket

FAILED_PART = "Failed password"
FOR_USER_PART = "for"
INVALID_USER_PART = "invalid user"
PORT_PART = "port"
FROM_IP_PART = "from"


def run():
    with open("/var/log/auth.log") as file:
        for _, line in enumerate(file):
            if FAILED_PART in line:
                user = get_user(line)
                port = get_port(line)
                ip_address = get_ip_address(line)
                timestamp = get_timestamp(line)

                print("{} attempted to connect on port {} from address {} on {}"
                      .format(user, port, ip_address, timestamp))


def get_user(line):
    connection_info = line.split(FOR_USER_PART)[1]

    if INVALID_USER_PART in connection_info:
        connection_info = connection_info.split(INVALID_USER_PART)[1]
    return connection_info.split(" ")[1]


def get_port(line):
    port_info = line.split(PORT_PART)[1]
    return port_info.split(" ")[1].strip()


def get_ip_address(line):
    ip_info = line.split(FROM_IP_PART)[1]
    return ip_info.split(" ")[1].strip()


def get_timestamp(line):
    return line.split(socket.gethostname())[0].strip()


run()

DATE=$(date +"%Y-%m-%d %H:%M")
speedtest-cli --simple > /Users/Holmes/bandwidth.log

echo "Running Speedtest now"

DOWN=$(grep Down /Users/Holmes/bandwidth.log | cut -d' ' -f2)
UP=$(grep Up /Users/Holmes/bandwidth.log | cut -d' ' -f2)

rm -f /Users/Holmes/bandwidth.log

echo "$DATE, $DOWN, $UP" >> /Users/Holmes/bandwidth_result.log

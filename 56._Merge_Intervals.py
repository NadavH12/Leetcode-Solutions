    def merge(self, intervals):
        #sort intervals by startpoint
        intervals.sort(key =lambda x: x[0])
        merged = []

        for interval in intervals:
            #if interval is first interval, add to merged list
            if (merged == []):
                merged.append(interval)
                continue
            
            
            latest_interval = merged[-1]

            latest_interval_endpoint = latest_interval[1]
            next_startpoint = interval[0]

            #if interval does not overlap with previous interval, simply add to merged list 
            if (latest_interval_endpoint < next_startpoint):
                merged.append(interval)
                continue

            #if interval does overlap, take the greater endpoint between the 2
            #set it as endpoint of merged interval
            #append new merged interval to merged list
            else: 
                latest_interval[1] = (max(merged[-1][-1], interval[1]))
                merged[-1] = latest_interval


        return merged


python2 filter.py ../data/image_class.txt ../data/rois/ ./ Histogram noPrint
matlab -nodesktop -r "classify(); quit"

python2 filter.py ../data/image_class.txt ../data/rois/ ./ log noPrint
matlab -nodesktop -r "classify(); quit"

python2 filter.py ../data/image_class.txt ../data/rois/ ./ boardHistogram noPrint
matlab -nodesktop -r "classify(); quit"

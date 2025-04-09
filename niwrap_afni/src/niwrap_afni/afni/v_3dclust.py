# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DCLUST_METADATA = Metadata(
    id="6ce131d0cf527a3a2a6df4f0ddf952eefa164b8c.boutiques",
    name="3dclust",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dclustParameters = typing.TypedDict('V3dclustParameters', {
    "__STYX_TYPE__": typing.Literal["3dclust"],
    "rmm": typing.NotRequired[float | None],
    "vmul": typing.NotRequired[float | None],
    "datasets": list[InputPathType],
    "nn1": bool,
    "nn2": bool,
    "nn3": bool,
    "noabs": bool,
    "summarize": bool,
    "nosum": bool,
    "verb": bool,
    "oned_format": bool,
    "no_oned_format": bool,
    "quiet": bool,
    "mni": bool,
    "isovalue": bool,
    "isomerge": bool,
    "inmask": bool,
    "prefix": typing.NotRequired[str | None],
    "savemask": typing.NotRequired[str | None],
    "binary": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "3dclust": v_3dclust_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "3dclust": v_3dclust_outputs,
    }.get(t)


class V3dclustOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dclust(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    prefixed_output: OutputPathType | None
    """New dataset with clusters set to zero based on prefix."""
    ordered_mask_output: OutputPathType | None
    """Ordered mask dataset based on savemask prefix."""


def v_3dclust_params(
    datasets: list[InputPathType],
    rmm: float | None = None,
    vmul: float | None = None,
    nn1: bool = False,
    nn2: bool = False,
    nn3: bool = False,
    noabs: bool = False,
    summarize: bool = False,
    nosum: bool = False,
    verb: bool = False,
    oned_format: bool = False,
    no_oned_format: bool = False,
    quiet: bool = False,
    mni: bool = False,
    isovalue: bool = False,
    isomerge: bool = False,
    inmask: bool = False,
    prefix: str | None = None,
    savemask: str | None = None,
    binary: bool = False,
) -> V3dclustParameters:
    """
    Build parameters.
    
    Args:
        datasets: Input dataset(s). More than one allowed, but only the first\
            sub-brick of the dataset.
        rmm: Cluster connection radius in millimeters.
        vmul: Minimum cluster volume in micro-liters or minimum number of\
            voxels if negative.
        nn1: 1st nearest-neighbor clustering (faces touching).
        nn2: 2nd nearest-neighbor clustering (edges touching).
        nn3: 3rd nearest-neighbor clustering (corners touching).
        noabs: Use the signed voxel intensities for calculations.
        summarize: Write out only the total nonzero voxel count and volume for\
            each dataset.
        nosum: Suppress printout of the totals.
        verb: Print out a progress report to stderr as computations proceed.
        oned_format: Write output in 1D format (default).
        no_oned_format: Do not write output in 1D format.
        quiet: Suppress all non-essential output.
        mni: Transform output xyz-coordinates from TLRC to MNI space if the\
            input dataset has the +tlrc view.
        isovalue: Clusters will be formed only from contiguous voxels that also\
            have the same value.
        isomerge: Clusters will be formed from each distinct value in the\
            dataset; spatial contiguity will not be used.
        inmask: Use an internal mask from the dataset to eliminate voxels\
            before clustering.
        prefix: Write a new dataset that is a copy of the input, but with all\
            voxels not in a cluster set to zero; provide a prefix for the new\
            dataset.
        savemask: Write a new dataset that is an ordered mask where the largest\
            cluster is labeled '1', the next largest '2', and so forth.
        binary: Turn the output of '-savemask' into a binary (0 or 1) mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dclust",
        "datasets": datasets,
        "nn1": nn1,
        "nn2": nn2,
        "nn3": nn3,
        "noabs": noabs,
        "summarize": summarize,
        "nosum": nosum,
        "verb": verb,
        "oned_format": oned_format,
        "no_oned_format": no_oned_format,
        "quiet": quiet,
        "mni": mni,
        "isovalue": isovalue,
        "isomerge": isomerge,
        "inmask": inmask,
        "binary": binary,
    }
    if rmm is not None:
        params["rmm"] = rmm
    if vmul is not None:
        params["vmul"] = vmul
    if prefix is not None:
        params["prefix"] = prefix
    if savemask is not None:
        params["savemask"] = savemask
    return params


def v_3dclust_cargs(
    params: V3dclustParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("3dclust")
    if params.get("rmm") is not None:
        cargs.append(str(params.get("rmm")))
    if params.get("vmul") is not None:
        cargs.append(str(params.get("vmul")))
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    if params.get("nn1"):
        cargs.append("-NN1")
    if params.get("nn2"):
        cargs.append("-NN2")
    if params.get("nn3"):
        cargs.append("-NN3")
    if params.get("noabs"):
        cargs.append("-noabs")
    if params.get("summarize"):
        cargs.append("-summarize")
    if params.get("nosum"):
        cargs.append("-nosum")
    if params.get("verb"):
        cargs.append("-verb")
    if params.get("oned_format"):
        cargs.append("-1Dformat")
    if params.get("no_oned_format"):
        cargs.append("-no_1Dformat")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("mni"):
        cargs.append("-mni")
    if params.get("isovalue"):
        cargs.append("-isovalue")
    if params.get("isomerge"):
        cargs.append("-isomerge")
    if params.get("inmask"):
        cargs.append("-inmask")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("savemask") is not None:
        cargs.extend([
            "-savemask",
            params.get("savemask")
        ])
    if params.get("binary"):
        cargs.append("-binary")
    return cargs


def v_3dclust_outputs(
    params: V3dclustParameters,
    execution: Execution,
) -> V3dclustOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dclustOutputs(
        root=execution.output_file("."),
        prefixed_output=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
        ordered_mask_output=execution.output_file(params.get("savemask") + ".nii.gz") if (params.get("savemask") is not None) else None,
    )
    return ret


def v_3dclust_execute(
    params: V3dclustParameters,
    execution: Execution,
) -> V3dclustOutputs:
    """
    Performs simple-minded cluster detection in 3D datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dclustOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dclust_cargs(params, execution)
    ret = v_3dclust_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dclust(
    datasets: list[InputPathType],
    rmm: float | None = None,
    vmul: float | None = None,
    nn1: bool = False,
    nn2: bool = False,
    nn3: bool = False,
    noabs: bool = False,
    summarize: bool = False,
    nosum: bool = False,
    verb: bool = False,
    oned_format: bool = False,
    no_oned_format: bool = False,
    quiet: bool = False,
    mni: bool = False,
    isovalue: bool = False,
    isomerge: bool = False,
    inmask: bool = False,
    prefix: str | None = None,
    savemask: str | None = None,
    binary: bool = False,
    runner: Runner | None = None,
) -> V3dclustOutputs:
    """
    Performs simple-minded cluster detection in 3D datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Input dataset(s). More than one allowed, but only the first\
            sub-brick of the dataset.
        rmm: Cluster connection radius in millimeters.
        vmul: Minimum cluster volume in micro-liters or minimum number of\
            voxels if negative.
        nn1: 1st nearest-neighbor clustering (faces touching).
        nn2: 2nd nearest-neighbor clustering (edges touching).
        nn3: 3rd nearest-neighbor clustering (corners touching).
        noabs: Use the signed voxel intensities for calculations.
        summarize: Write out only the total nonzero voxel count and volume for\
            each dataset.
        nosum: Suppress printout of the totals.
        verb: Print out a progress report to stderr as computations proceed.
        oned_format: Write output in 1D format (default).
        no_oned_format: Do not write output in 1D format.
        quiet: Suppress all non-essential output.
        mni: Transform output xyz-coordinates from TLRC to MNI space if the\
            input dataset has the +tlrc view.
        isovalue: Clusters will be formed only from contiguous voxels that also\
            have the same value.
        isomerge: Clusters will be formed from each distinct value in the\
            dataset; spatial contiguity will not be used.
        inmask: Use an internal mask from the dataset to eliminate voxels\
            before clustering.
        prefix: Write a new dataset that is a copy of the input, but with all\
            voxels not in a cluster set to zero; provide a prefix for the new\
            dataset.
        savemask: Write a new dataset that is an ordered mask where the largest\
            cluster is labeled '1', the next largest '2', and so forth.
        binary: Turn the output of '-savemask' into a binary (0 or 1) mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dclustOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DCLUST_METADATA)
    params = v_3dclust_params(
        rmm=rmm,
        vmul=vmul,
        datasets=datasets,
        nn1=nn1,
        nn2=nn2,
        nn3=nn3,
        noabs=noabs,
        summarize=summarize,
        nosum=nosum,
        verb=verb,
        oned_format=oned_format,
        no_oned_format=no_oned_format,
        quiet=quiet,
        mni=mni,
        isovalue=isovalue,
        isomerge=isomerge,
        inmask=inmask,
        prefix=prefix,
        savemask=savemask,
        binary=binary,
    )
    return v_3dclust_execute(params, execution)


__all__ = [
    "V3dclustOutputs",
    "V3dclustParameters",
    "V_3DCLUST_METADATA",
    "v_3dclust",
    "v_3dclust_params",
]

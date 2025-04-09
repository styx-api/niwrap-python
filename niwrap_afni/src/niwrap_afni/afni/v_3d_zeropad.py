# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ZEROPAD_METADATA = Metadata(
    id="8becb29cf5d687af1a0c52c165ec0b440d32f49e.boutiques",
    name="3dZeropad",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dZeropadParameters = typing.TypedDict('V3dZeropadParameters', {
    "__STYX_TYPE__": typing.Literal["3dZeropad"],
    "dataset": InputPathType,
    "I": typing.NotRequired[float | None],
    "S": typing.NotRequired[float | None],
    "A": typing.NotRequired[float | None],
    "P": typing.NotRequired[float | None],
    "L": typing.NotRequired[float | None],
    "R": typing.NotRequired[float | None],
    "z": typing.NotRequired[float | None],
    "RL": typing.NotRequired[float | None],
    "AP": typing.NotRequired[float | None],
    "IS": typing.NotRequired[float | None],
    "pad2even": bool,
    "mm_flag": bool,
    "master_dataset": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
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
        "3dZeropad": v_3d_zeropad_cargs,
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
        "3dZeropad": v_3d_zeropad_outputs,
    }.get(t)


class V3dZeropadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zeropad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_brik: OutputPathType | None
    """Output dataset (BRIK format)"""
    output_dataset_head: OutputPathType | None
    """Output dataset (HEAD format)"""


def v_3d_zeropad_params(
    dataset: InputPathType,
    i: float | None = None,
    s: float | None = None,
    a: float | None = None,
    p: float | None = None,
    l: float | None = None,
    r: float | None = None,
    z: float | None = None,
    rl: float | None = None,
    ap: float | None = None,
    is_: float | None = None,
    pad2even: bool = False,
    mm_flag: bool = False,
    master_dataset: InputPathType | None = None,
    prefix: str | None = None,
) -> V3dZeropadParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset.
        i: Adds 'n' planes of zero at the Inferior edge.
        s: Adds 'n' planes of zero at the Superior edge.
        a: Adds 'n' planes of zero at the Anterior edge.
        p: Adds 'n' planes of zero at the Posterior edge.
        l: Adds 'n' planes of zero at the Left edge.
        r: Adds 'n' planes of zero at the Right edge.
        z: Adds 'n' planes of zeros on EACH of the dataset z-axis\
            (slice-direction) faces.
        rl: Add/cut planes symmetrically to make the resulting volume have 'a'\
            slices in the Right/Left direction.
        ap: Add/cut planes symmetrically to make the resulting volume have 'b'\
            slices in the Anterior/Posterior direction.
        is_: Add/cut planes symmetrically to make the resulting volume have 'c'\
            slices in the Inferior/Superior direction.
        pad2even: Add 0 or 1 plane in each of the R/A/S directions, giving each\
            axis an even number of slices.
        mm_flag: Pad counts 'n' are in mm instead of slices.
        master_dataset: Match the volume described in dataset 'mset'. 'mset'\
            must have the same orientation and grid spacing as dataset to be\
            padded.
        prefix: Write result into dataset with prefix 'ppp'. Default is\
            'zeropad'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dZeropad",
        "dataset": dataset,
        "pad2even": pad2even,
        "mm_flag": mm_flag,
    }
    if i is not None:
        params["I"] = i
    if s is not None:
        params["S"] = s
    if a is not None:
        params["A"] = a
    if p is not None:
        params["P"] = p
    if l is not None:
        params["L"] = l
    if r is not None:
        params["R"] = r
    if z is not None:
        params["z"] = z
    if rl is not None:
        params["RL"] = rl
    if ap is not None:
        params["AP"] = ap
    if is_ is not None:
        params["IS"] = is_
    if master_dataset is not None:
        params["master_dataset"] = master_dataset
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_zeropad_cargs(
    params: V3dZeropadParameters,
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
    cargs.append("3dZeropad")
    cargs.append(execution.input_file(params.get("dataset")))
    if params.get("I") is not None:
        cargs.extend([
            "-I",
            str(params.get("I"))
        ])
    if params.get("S") is not None:
        cargs.extend([
            "-S",
            str(params.get("S"))
        ])
    if params.get("A") is not None:
        cargs.extend([
            "-A",
            str(params.get("A"))
        ])
    if params.get("P") is not None:
        cargs.extend([
            "-P",
            str(params.get("P"))
        ])
    if params.get("L") is not None:
        cargs.extend([
            "-L",
            str(params.get("L"))
        ])
    if params.get("R") is not None:
        cargs.extend([
            "-R",
            str(params.get("R"))
        ])
    if params.get("z") is not None:
        cargs.extend([
            "-z",
            str(params.get("z"))
        ])
    if params.get("RL") is not None:
        cargs.extend([
            "-RL",
            str(params.get("RL"))
        ])
    if params.get("AP") is not None:
        cargs.extend([
            "-AP",
            str(params.get("AP"))
        ])
    if params.get("IS") is not None:
        cargs.extend([
            "-IS",
            str(params.get("IS"))
        ])
    if params.get("pad2even"):
        cargs.append("-pad2evens")
    if params.get("mm_flag"):
        cargs.append("-mm")
    if params.get("master_dataset") is not None:
        cargs.extend([
            "-master",
            execution.input_file(params.get("master_dataset"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def v_3d_zeropad_outputs(
    params: V3dZeropadParameters,
    execution: Execution,
) -> V3dZeropadOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dZeropadOutputs(
        root=execution.output_file("."),
        output_dataset_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
        output_dataset_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_zeropad_execute(
    params: V3dZeropadParameters,
    execution: Execution,
) -> V3dZeropadOutputs:
    """
    Adds planes of zeros to a dataset (i.e., pads it out). Negative 'add' count
    means to cut a dataset down in size.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dZeropadOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_zeropad_cargs(params, execution)
    ret = v_3d_zeropad_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_zeropad(
    dataset: InputPathType,
    i: float | None = None,
    s: float | None = None,
    a: float | None = None,
    p: float | None = None,
    l: float | None = None,
    r: float | None = None,
    z: float | None = None,
    rl: float | None = None,
    ap: float | None = None,
    is_: float | None = None,
    pad2even: bool = False,
    mm_flag: bool = False,
    master_dataset: InputPathType | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dZeropadOutputs:
    """
    Adds planes of zeros to a dataset (i.e., pads it out). Negative 'add' count
    means to cut a dataset down in size.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        i: Adds 'n' planes of zero at the Inferior edge.
        s: Adds 'n' planes of zero at the Superior edge.
        a: Adds 'n' planes of zero at the Anterior edge.
        p: Adds 'n' planes of zero at the Posterior edge.
        l: Adds 'n' planes of zero at the Left edge.
        r: Adds 'n' planes of zero at the Right edge.
        z: Adds 'n' planes of zeros on EACH of the dataset z-axis\
            (slice-direction) faces.
        rl: Add/cut planes symmetrically to make the resulting volume have 'a'\
            slices in the Right/Left direction.
        ap: Add/cut planes symmetrically to make the resulting volume have 'b'\
            slices in the Anterior/Posterior direction.
        is_: Add/cut planes symmetrically to make the resulting volume have 'c'\
            slices in the Inferior/Superior direction.
        pad2even: Add 0 or 1 plane in each of the R/A/S directions, giving each\
            axis an even number of slices.
        mm_flag: Pad counts 'n' are in mm instead of slices.
        master_dataset: Match the volume described in dataset 'mset'. 'mset'\
            must have the same orientation and grid spacing as dataset to be\
            padded.
        prefix: Write result into dataset with prefix 'ppp'. Default is\
            'zeropad'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZeropadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZEROPAD_METADATA)
    params = v_3d_zeropad_params(
        dataset=dataset,
        i=i,
        s=s,
        a=a,
        p=p,
        l=l,
        r=r,
        z=z,
        rl=rl,
        ap=ap,
        is_=is_,
        pad2even=pad2even,
        mm_flag=mm_flag,
        master_dataset=master_dataset,
        prefix=prefix,
    )
    return v_3d_zeropad_execute(params, execution)


__all__ = [
    "V3dZeropadOutputs",
    "V3dZeropadParameters",
    "V_3D_ZEROPAD_METADATA",
    "v_3d_zeropad",
    "v_3d_zeropad_params",
]

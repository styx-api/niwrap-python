# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TSGEN_METADATA = Metadata(
    id="23ea0ec274045284df882fa88ec58e47ba43443f.boutiques",
    name="3dTSgen",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dTsgenParameters = typing.TypedDict('V3dTsgenParameters', {
    "__STYX_TYPE__": typing.Literal["3dTSgen"],
    "input_file": InputPathType,
    "in_tr_flag": bool,
    "signal_label": str,
    "noise_label": str,
    "signal_constr": typing.NotRequired[str | None],
    "noise_constr": typing.NotRequired[str | None],
    "sigma_value": float,
    "voxel_number": typing.NotRequired[float | None],
    "output_file": str,
    "signal_coef": typing.NotRequired[str | None],
    "noise_coef": typing.NotRequired[str | None],
    "bucket_config": typing.NotRequired[str | None],
    "brick_config": typing.NotRequired[str | None],
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
        "3dTSgen": v_3d_tsgen_cargs,
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
    }.get(t)


class V3dTsgenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tsgen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_tsgen_params(
    input_file: InputPathType,
    signal_label: str,
    noise_label: str,
    sigma_value: float,
    output_file: str,
    in_tr_flag: bool = False,
    signal_constr: str | None = None,
    noise_constr: str | None = None,
    voxel_number: float | None = None,
    signal_coef: str | None = None,
    noise_coef: str | None = None,
    bucket_config: str | None = None,
    brick_config: str | None = None,
) -> V3dTsgenParameters:
    """
    Build parameters.
    
    Args:
        input_file: Filename of prototype 3d + time data file.
        signal_label: Name of the (non-linear) signal model.
        noise_label: Name of the (linear) noise model.
        sigma_value: Standard deviation of additive Gaussian noise.
        output_file: Filename of output 3d + time data file.
        in_tr_flag: Set the TR of the created timeseries to be the TR of the\
            prototype dataset. The default is TR = 1.
        signal_constr: Constraints for kth signal parameter. Format: k c d\
            where c <= gs[k] <= d.
        noise_constr: Constraints for kth noise parameter. Format: k c d where\
            c+b[k] <= gn[k] <= d+b[k].
        voxel_number: Screen output for voxel number.
        signal_coef: Write kth signal parameter gs[k]. Output 'fim' is written\
            to prefix filename.
        noise_coef: Write kth noise parameter gn[k]. Output 'fim' is written to\
            prefix filename.
        bucket_config: Create one AFNI 'bucket' dataset containing n\
            sub-bricks. n=0 creates the default output. Output 'bucket' is written\
            to prefixname.
        brick_config: Specify content for sub-brick in the form 'm t k label'\
            where m is the sub-brick number, t is 'scoef' or 'ncoef', k is\
            parameter index, and label is a descriptive label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTSgen",
        "input_file": input_file,
        "in_tr_flag": in_tr_flag,
        "signal_label": signal_label,
        "noise_label": noise_label,
        "sigma_value": sigma_value,
        "output_file": output_file,
    }
    if signal_constr is not None:
        params["signal_constr"] = signal_constr
    if noise_constr is not None:
        params["noise_constr"] = noise_constr
    if voxel_number is not None:
        params["voxel_number"] = voxel_number
    if signal_coef is not None:
        params["signal_coef"] = signal_coef
    if noise_coef is not None:
        params["noise_coef"] = noise_coef
    if bucket_config is not None:
        params["bucket_config"] = bucket_config
    if brick_config is not None:
        params["brick_config"] = brick_config
    return params


def v_3d_tsgen_cargs(
    params: V3dTsgenParameters,
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
    cargs.append("3dTSgen")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("in_tr_flag"):
        cargs.append("-inTR")
    cargs.extend([
        "-signal",
        params.get("signal_label")
    ])
    cargs.extend([
        "-noise",
        params.get("noise_label")
    ])
    if params.get("signal_constr") is not None:
        cargs.extend([
            "-sconstr",
            params.get("signal_constr")
        ])
    if params.get("noise_constr") is not None:
        cargs.extend([
            "-nconstr",
            params.get("noise_constr")
        ])
    cargs.extend([
        "-sigma",
        str(params.get("sigma_value"))
    ])
    if params.get("voxel_number") is not None:
        cargs.extend([
            "-voxel",
            str(params.get("voxel_number"))
        ])
    cargs.extend([
        "-output",
        params.get("output_file")
    ])
    if params.get("signal_coef") is not None:
        cargs.extend([
            "-scoef",
            params.get("signal_coef")
        ])
    if params.get("noise_coef") is not None:
        cargs.extend([
            "-ncoef",
            params.get("noise_coef")
        ])
    if params.get("bucket_config") is not None:
        cargs.extend([
            "-bucket",
            params.get("bucket_config")
        ])
    if params.get("brick_config") is not None:
        cargs.extend([
            "-brick",
            params.get("brick_config")
        ])
    return cargs


def v_3d_tsgen_outputs(
    params: V3dTsgenParameters,
    execution: Execution,
) -> V3dTsgenOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTsgenOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_tsgen_execute(
    params: V3dTsgenParameters,
    execution: Execution,
) -> V3dTsgenOutputs:
    """
    This program generates an AFNI 3d+time data set based on user-specified signal
    and noise models for each voxel.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTsgenOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tsgen_cargs(params, execution)
    ret = v_3d_tsgen_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tsgen(
    input_file: InputPathType,
    signal_label: str,
    noise_label: str,
    sigma_value: float,
    output_file: str,
    in_tr_flag: bool = False,
    signal_constr: str | None = None,
    noise_constr: str | None = None,
    voxel_number: float | None = None,
    signal_coef: str | None = None,
    noise_coef: str | None = None,
    bucket_config: str | None = None,
    brick_config: str | None = None,
    runner: Runner | None = None,
) -> V3dTsgenOutputs:
    """
    This program generates an AFNI 3d+time data set based on user-specified signal
    and noise models for each voxel.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Filename of prototype 3d + time data file.
        signal_label: Name of the (non-linear) signal model.
        noise_label: Name of the (linear) noise model.
        sigma_value: Standard deviation of additive Gaussian noise.
        output_file: Filename of output 3d + time data file.
        in_tr_flag: Set the TR of the created timeseries to be the TR of the\
            prototype dataset. The default is TR = 1.
        signal_constr: Constraints for kth signal parameter. Format: k c d\
            where c <= gs[k] <= d.
        noise_constr: Constraints for kth noise parameter. Format: k c d where\
            c+b[k] <= gn[k] <= d+b[k].
        voxel_number: Screen output for voxel number.
        signal_coef: Write kth signal parameter gs[k]. Output 'fim' is written\
            to prefix filename.
        noise_coef: Write kth noise parameter gn[k]. Output 'fim' is written to\
            prefix filename.
        bucket_config: Create one AFNI 'bucket' dataset containing n\
            sub-bricks. n=0 creates the default output. Output 'bucket' is written\
            to prefixname.
        brick_config: Specify content for sub-brick in the form 'm t k label'\
            where m is the sub-brick number, t is 'scoef' or 'ncoef', k is\
            parameter index, and label is a descriptive label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTsgenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TSGEN_METADATA)
    params = v_3d_tsgen_params(
        input_file=input_file,
        in_tr_flag=in_tr_flag,
        signal_label=signal_label,
        noise_label=noise_label,
        signal_constr=signal_constr,
        noise_constr=noise_constr,
        sigma_value=sigma_value,
        voxel_number=voxel_number,
        output_file=output_file,
        signal_coef=signal_coef,
        noise_coef=noise_coef,
        bucket_config=bucket_config,
        brick_config=brick_config,
    )
    return v_3d_tsgen_execute(params, execution)


__all__ = [
    "V3dTsgenOutputs",
    "V3dTsgenParameters",
    "V_3D_TSGEN_METADATA",
    "v_3d_tsgen",
    "v_3d_tsgen_params",
]

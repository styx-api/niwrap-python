# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_PARCEL_RESAMPLING_METADATA = Metadata(
    id="05f92ef977b53987cf5dd7d77550664f10e2cf24.boutiques",
    name="volume-parcel-resampling",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


VolumeParcelResamplingParameters = typing.TypedDict('VolumeParcelResamplingParameters', {
    "__STYXTYPE__": typing.Literal["volume-parcel-resampling"],
    "volume_in": InputPathType,
    "cur_parcels": InputPathType,
    "new_parcels": InputPathType,
    "kernel": float,
    "volume_out": str,
    "opt_fix_zeros": bool,
    "opt_fwhm": bool,
    "opt_subvolume_subvol": typing.NotRequired[str | None],
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
        "volume-parcel-resampling": volume_parcel_resampling_cargs,
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
        "volume-parcel-resampling": volume_parcel_resampling_outputs,
    }.get(t)


class VolumeParcelResamplingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_parcel_resampling(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """output volume"""


def volume_parcel_resampling_params(
    volume_in: InputPathType,
    cur_parcels: InputPathType,
    new_parcels: InputPathType,
    kernel: float,
    volume_out: str,
    opt_fix_zeros: bool = False,
    opt_fwhm: bool = False,
    opt_subvolume_subvol: str | None = None,
) -> VolumeParcelResamplingParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the input data volume.
        cur_parcels: label volume of where the parcels currently are.
        new_parcels: label volume of where the parcels should be.
        kernel: gaussian kernel size in mm to smooth by during resampling, as\
            sigma by default.
        volume_out: output volume.
        opt_fix_zeros: treat zero values as not being data.
        opt_fwhm: smoothing kernel size is FWHM, not sigma.
        opt_subvolume_subvol: select a single subvolume as input: the subvolume\
            number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-parcel-resampling",
        "volume_in": volume_in,
        "cur_parcels": cur_parcels,
        "new_parcels": new_parcels,
        "kernel": kernel,
        "volume_out": volume_out,
        "opt_fix_zeros": opt_fix_zeros,
        "opt_fwhm": opt_fwhm,
    }
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    return params


def volume_parcel_resampling_cargs(
    params: VolumeParcelResamplingParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-parcel-resampling")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(execution.input_file(params.get("cur_parcels")))
    cargs.append(execution.input_file(params.get("new_parcels")))
    cargs.append(str(params.get("kernel")))
    cargs.append(params.get("volume_out"))
    if params.get("opt_fix_zeros"):
        cargs.append("-fix-zeros")
    if params.get("opt_fwhm"):
        cargs.append("-fwhm")
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    return cargs


def volume_parcel_resampling_outputs(
    params: VolumeParcelResamplingParameters,
    execution: Execution,
) -> VolumeParcelResamplingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeParcelResamplingOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_parcel_resampling_execute(
    params: VolumeParcelResamplingParameters,
    execution: Execution,
) -> VolumeParcelResamplingOutputs:
    """
    Smooth and resample volume parcels.
    
    Smooths and resamples the region inside each label in cur-parcels to the
    region of the same label name in new-parcels. Any voxels in the output label
    region but outside the input label region will be extrapolated from nearby
    data. The -fix-zeros option causes the smoothing to not use an input value
    if it is zero, but still write a smoothed value to the voxel, and after
    smoothing is complete, it will check for any remaining values of zero, and
    fill them in with extrapolated values.
    
    Note: all volumes must have the same dimensions and spacing. To use a
    different output space, see -volume-parcel-resampling-generic.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeParcelResamplingOutputs`).
    """
    params = execution.params(params)
    cargs = volume_parcel_resampling_cargs(params, execution)
    ret = volume_parcel_resampling_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_parcel_resampling(
    volume_in: InputPathType,
    cur_parcels: InputPathType,
    new_parcels: InputPathType,
    kernel: float,
    volume_out: str,
    opt_fix_zeros: bool = False,
    opt_fwhm: bool = False,
    opt_subvolume_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeParcelResamplingOutputs:
    """
    Smooth and resample volume parcels.
    
    Smooths and resamples the region inside each label in cur-parcels to the
    region of the same label name in new-parcels. Any voxels in the output label
    region but outside the input label region will be extrapolated from nearby
    data. The -fix-zeros option causes the smoothing to not use an input value
    if it is zero, but still write a smoothed value to the voxel, and after
    smoothing is complete, it will check for any remaining values of zero, and
    fill them in with extrapolated values.
    
    Note: all volumes must have the same dimensions and spacing. To use a
    different output space, see -volume-parcel-resampling-generic.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input data volume.
        cur_parcels: label volume of where the parcels currently are.
        new_parcels: label volume of where the parcels should be.
        kernel: gaussian kernel size in mm to smooth by during resampling, as\
            sigma by default.
        volume_out: output volume.
        opt_fix_zeros: treat zero values as not being data.
        opt_fwhm: smoothing kernel size is FWHM, not sigma.
        opt_subvolume_subvol: select a single subvolume as input: the subvolume\
            number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeParcelResamplingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_PARCEL_RESAMPLING_METADATA)
    params = volume_parcel_resampling_params(
        volume_in=volume_in,
        cur_parcels=cur_parcels,
        new_parcels=new_parcels,
        kernel=kernel,
        volume_out=volume_out,
        opt_fix_zeros=opt_fix_zeros,
        opt_fwhm=opt_fwhm,
        opt_subvolume_subvol=opt_subvolume_subvol,
    )
    return volume_parcel_resampling_execute(params, execution)


__all__ = [
    "VOLUME_PARCEL_RESAMPLING_METADATA",
    "VolumeParcelResamplingOutputs",
    "VolumeParcelResamplingParameters",
    "volume_parcel_resampling",
    "volume_parcel_resampling_params",
]
